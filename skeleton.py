

    Make a copy of your skeleton directory. Name it after your new project.
    Rename (move) the NAME directory to be the name of your project or whatever you want to call your root module.
    Edit your setup.py to have all the information for your project.
    Rename tests/NAME_tests.py to also have your module name.
    Double check it's all working by using nosetests again.
    Start coding.

    Virtual environment - say you have a project that uses Firefox 2.1 but then
    another project started later uses 4.2. If you update your whole system
    the old project might not work anymore. In a virtual environment you can still
    use the old version for the old project.

    In setup.py, put package name and script location as demonstrated. Script should
    be in the bin folder. Name folder should be called after package name and just
    have init file in it. Test folder should have init and package name tests files
    Name tests should include name of your package after import, such as Import
    hello

    One whole skeleton directory per project, named after project

    A bin folder is a standard place to put scripts that are run on thecommand line,
    not a place to put modules

# activate the virtual environment with this
.\.venvs\lpthw\Scripts\activate
