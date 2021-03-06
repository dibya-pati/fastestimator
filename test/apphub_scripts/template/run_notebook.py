import os

if __name__ == "__main__":
    """The template for running apphub Jupyter notebook sample. Users only need to fill the sections with comments.
    """
    apphub_path = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "apphub"))
    example_name = ""  # The name of the running example. It should match the jupyter notebook file name.

    source_dir = os.path.join(apphub_path, "", "")  # The path to that example directory
    stderr_file = os.path.abspath(os.path.join(__file__, "..", "run_notebook.txt"))
    if os.path.exists(stderr_file):
        os.remove(stderr_file)

    nb_in_file = os.path.join(source_dir, example_name + ".ipynb")
    nb_out_file = os.path.abspath(os.path.join(__file__, "..", example_name + "_out.ipynb"))

    train_info = ""  # The training arguments
    # Usually we set the epochs:2, batch_size:2, steps_per_epoch:10, validation_steps:5
    # The expression for the following setup is "-p epochs 2 -p batch_size 2 -p steps_per_epoch 10 -p validation_steps 5"
    # The arguement will re-declare the variable right after the jupyter notebook cell with "parameters" tag (there must
    # be one and only cell with "parameters" tag)
    # The syntax of this expression is different from run_notebook.py

    result = os.system("papermill {} {} {} -k nightly-build 2>> {}".format(nb_in_file, nb_out_file, train_info, stderr_file))

    if result:
        raise ValueError("{} fail".format(nb_in_file))