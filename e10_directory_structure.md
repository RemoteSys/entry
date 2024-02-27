## Directory structure

Scripts created during classes should be organized in the structure shown below.

1. Rename the `example_proj` directory with the name from your project.

2. Place the python modules in the `src` directory:
   - divide the code into modules according to tasks, e.g. separate functions supporting different data formats

3. Place template files for the report in the `templates` directory.


<style>
 .green {
    color: #CC9900;
}
</style>

<pre>
<span class="green">C:\python_courses\</span>                    - main python course folder
|
+---<span class="green">\projects\</span>                        - directory with exercises/projects
    |   
    +---<span class="green">\example_proj\</span>              - project folder: data format conversion (csv, json, xml)
        |    pyproject.toml           - configuration file for script installation
        |    requirements.txt         - file for `pip` manager: list of modules to be installed
        |                               in the script's virtual environment
        |    README.md                - a file with a description of the project and how the script works
        |    
        +----<span class="green">\env_example_proj\</span>     - directory with the installed virtual environment
        +----<span class="green">\example_proj\</span>         - python package: directory containing python files
             |    main.py             - main script file
             |    
             +----<span class="green">\src\</span>             - directory with python modules
                  |    parser.py
                  |    my_mod1.py
                  |    my_mod2.py
                  |    my_mod3.py
                  |
                  <span class="green">\templates\</span>        - directory with report template files
                       template1.md
                       template2.md
</pre>


