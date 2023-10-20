import mkdocs_macros
import os

def define_env(env):
    "Hook function"

    # We want a relative docs_dir and not an absolute path to it, for security
    # reasons
    docs_dir = env.variables["config"]["docs_dir"].split('/')[-1] + '/'

    # Directory of public datasets. Can be either absolute or relative to docs_dir
    public_dir = "static/public_datasets/"
    # Directory of protected datasets. Can be either absolute or relative to docs_dir
    protected_dir = "static/protected_datasets/"

    def list_files(relpath):
        # Returns a markdown list of downloadable files in relpath, where
        # relpath is relative to docs_dir
        dataset_files = sorted(os.listdir(docs_dir+relpath))
        markdown = ""
        for file in dataset_files:
            sha256sum = ""
            markdown += f"* [{file}]({relpath}/{file}){{download={file}}} {sha256sum}\n"
        return markdown
    

    @env.macro
    def show_public_datasets():
        return list_files(public_dir)
    
    @env.macro
    def show_protected_datasets():
        return list_files(protected_dir)