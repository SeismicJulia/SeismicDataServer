import os
import mkdocs_macros

from util import *

def define_env(env):
    "Hook function"

    # We want a relative docs_dir and not an absolute path to it, for security
    # reasons
    #docs_dir = env.variables["config"]["docs_dir"] + '/'

    # nfs_dir is the true directory of the dataset files, aliased_dir is the directory
    # that shows up on the web page. Note that aliased_dir must be redirected to nfs_dir 
    # in the web server config file
    nfs_dir = "/nfs/Datasets"
    aliased_dir = "/static/Datasets"

    # Directory of public datasets. Can be either absolute or relative to docs_dir
    public_dir = "Public"
    # Directory of private datasets. Can be either absolute or relative to docs_dir
    private_dir = "Private"
    # Directory of testing datasets. Can be either absolute or relative to docs_dir
    testing_dir = "Testing"
    
    # Files that don't pass checksum tests
    failed_checksums = []

    def list_files(dir_name):
        # Returns a markdown list of downloadable files in relpath, where
        # relpath is relative to docs_dir
        dataset_files = sorted(filename for filename in os.listdir(f"{nfs_dir}/{dir_name}") if filename[0] != '.')
        page_markdown = ""
        for file in dataset_files:
            filepath = f"{nfs_dir}/{dir_name}/{file}"
            sha256sum = compute_checksum(filepath, "sha256")
            if verify_checksum(filepath, sha256sum):
                file_size = human_readable_file_size(filepath)
                description = get_file_description(filepath)
                download_link = f"[{file}]({aliased_dir}/{dir_name}/{file}){{:download={file}}}"
                file_markdown = [
                    f"* {download_link}",
                    f"      * Checksum: sha256-{sha256sum}",
                    f"      * Size: {file_size}",
                    f"      * Description: {description}",
                    '' # Empty string at the end to make sure there is a newline after the last item
                ]
                page_markdown += '\n'.join(file_markdown)
            else:
                failed_checksums.append(filepath)
        return page_markdown

    public_datasets_md = list_files(public_dir)
    private_datasets_md = list_files(private_dir)
    testing_datasets_md = list_files(testing_dir)
    
    @env.macro
    def show_public_datasets():
        return public_datasets_md
    
    @env.macro
    def show_private_datasets():
        return private_datasets_md
    
    @env.macro
    def show_testing_datasets():
        return testing_datasets_md
    
    @env.macro
    def show_warnings():
        # If any files failed the checksum test, display a warning in the admin dashboard
        if failed_checksums:
            failed_checksums_md = '\n\t\t'.join(failed_checksums)
            admonition = f"??? failure \"Failed Checksum Test\"\n\t```\n\t\t{failed_checksums_md}\n\t```"
            return admonition
        return ""