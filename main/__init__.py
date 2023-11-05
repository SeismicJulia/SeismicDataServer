import os
import mkdocs_macros

from util import *

def define_env(env):
    "Hook function"

    # We want a relative docs_dir and not an absolute path to it, for security
    # reasons
    docs_dir = env.variables["config"]["docs_dir"] + '/'

    # Directory of public datasets. Can be either absolute or relative to docs_dir
    public_dir = "static/public_datasets/"
    # Directory of protected datasets. Can be either absolute or relative to docs_dir
    private_dir = "static/private_datasets/"
    
    # Files that don't pass checksum tests
    failed_checksums = []

    def list_files(relpath):
        # Returns a markdown list of downloadable files in relpath, where
        # relpath is relative to docs_dir
        dataset_files = sorted(filename for filename in os.listdir(docs_dir+relpath) if filename[0] != '.')
        page_markdown = ""
        for file in dataset_files:
            filepath = f"{docs_dir}{relpath}{file}"
            sha256sum = compute_checksum(filepath, "sha256")
            if verify_checksum(filepath, sha256sum):
                file_size = human_readable_file_size(filepath)
                # Note the starting '/' below
                download_link = f"[{file}](/{relpath}{file}){{:download={file}}}"
                file_markdown = [
                    f"* {download_link}",
                    f"      * Checksum: sha256-{sha256sum}",
                    f"      * Size: {file_size}",
                    '' # Empty string at the end to make sure there is a newline after the last item
                ]
                page_markdown += '\n'.join(file_markdown)
            else:
                failed_checksums.append(filepath)
        return page_markdown

    public_datasets_md = list_files(public_dir)
    private_datasets_md = list_files(private_dir)
    
    @env.macro
    def show_public_datasets():
        return public_datasets_md
    
    @env.macro
    def show_protected_datasets():
        return private_datasets_md
    
    @env.macro
    def show_warnings():
        # If any files failed the checksum test, display a warning in the admin dashboard
        if failed_checksums:
            failed_checksums_md = '\n\t\t'.join(failed_checksums)
            admonition = f"??? failure \"Failed Checksum Test\"\n\t```\n\t\t{failed_checksums_md}\n\t```"
            return admonition
        return ""