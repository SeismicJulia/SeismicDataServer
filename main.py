import os, hashlib
import mkdocs_macros

def define_env(env):
    "Hook function"

    # We want a relative docs_dir and not an absolute path to it, for security
    # reasons
    docs_dir = env.variables["config"]["docs_dir"] + '/'

    # Directory of public datasets. Can be either absolute or relative to docs_dir
    public_dir = "static/public_datasets/"
    # Directory of protected datasets. Can be either absolute or relative to docs_dir
    protected_dir = "static/protected_datasets/"

    def compute_checksum(filepath, algorithm):
        # filepath is the path of the file for which the checksum is to be computed
        # algorithm is the algorithm we want to use to compute the checksum (see
        # hashlib.new() documentation: https://docs.python.org/3/library/hashlib.html#hashlib.new)
        checksum = hashlib.new(algorithm)
        buffer_size = 2**16  # 64 KB

        with open(filepath, "rb") as f:
            data = f.read(buffer_size)
            while data:
                checksum.update(data)
                data = f.read(buffer_size)
        
        return checksum.hexdigest()

    def list_files(relpath):
        # Returns a markdown list of downloadable files in relpath, where
        # relpath is relative to docs_dir
        dataset_files = sorted(os.listdir(docs_dir+relpath))
        markdown = ""
        for file in dataset_files:
            filepath = f"{docs_dir}{relpath}{file}"
            sha256sum = compute_checksum(filepath, "sha256")
            markdown += f"* [{file}]({relpath}/{file}){{:download={file}}} sha256-{sha256sum}\n"
        return markdown
    

    @env.macro
    def show_public_datasets():
        return list_files(public_dir)
    
    @env.macro
    def show_protected_datasets():
        return list_files(protected_dir)