# Archived Jupyter Bookmaker

This repository has been archived. The project continues, under a different name, in [nbbinder](https://github.com/rmsrosa/nbbinder).

## Reason for archiving

I never liked the name `jupyterbookmaker`. And since "bookmaker" has a meaning different than "producing a book", this name turned out to be innapropriate.

I also thought about `jupyterbookbinder`, but I was reluctant to use a name associated with `binder` because of the [mybinder](https://mybinder.org/) project. But "binder" is indeed a more appropriate name. And there shouldn't be much conflict upon adding words to it, as in `jupyterbookbinder`. But this is still a long name, which also bothered me. So I finally settled for `notebook binder`, or `nbbinder`, for short.

I could have thus simply renamed the repository to `nbbinder`, but I thought it was best to simply archive this one.

## Description

Generates a navigable book-like structure to a collection of Jupyter notebooks.

It adds a Table of Contents to a given "Table of Contents" file, and adds a header and top and bottom navigator cells to each notebook.

## The collection of notebooks

The code works on a collection of indexed notebooks in a directory and builds a Table of Contents out of the them, which is added to a specified file. It also adds a header and top and bottom navigator cells to each notebook.

In order to be indexed, the notebooks should be of one the following forms:

- `'dd.dd-notebookname.ipynb'`, where `'d'` is any decimal from 0 to 9;
- `'dd.-notebookname.ipynb'`, where `'d'` is as above;
- `'AX.dd-notebookname.ipynb'`, where `'d'` is as above, `'A'` is the uppercase letter `'A'` and `'X'` is any uppercase letter;
- `'AX.-notebookname.ipynb'`, where the symbols are as above;
- `'BX.dd-notebookname.ipynb'`, where `'B'` is the upper case letter `'B'` and the rest is as above; or
- `'BX.-notebookname.ipynb'`, where the symbols are as above.

The filenames go through a regular expressions matching operator and three groups are extracted from them, as separated by the first two dots.

- When the first group is `'00'`, the notebook appears in the beginning and is not numbered. It is for the **Front Matter**, e.g *Cover page*, *Copyright page*, *Dedication page*, *Epigraph*, *Table of Contents*, *Foreword*, *Preface*, *Acknowlegdments*, and so on.
- When the first group is from `'10'` to `'99'`, it is for the **Body** of the book, with the first group representing the chapter number and the second group, the section number. Except when the second group is either the empty string '' or '00', in which cases there is no section number. These are useful for defining a *Part* of the book and an introduction to the chapter, respectively. Notice that '' comes before '00'.
- When the first group starts with `'A'`, it is assumed to be for an **Appendix**, in which the second letter `'X'` is the letter of the Appendix. The second group functions as the section of the Appendix, with the same exceptions as above in the cases in which the second group is either `''` or `'00'`.
- When the first group starts with `'B'`, the notebook appears at the end and is not numbered. It is for the non-numbered part of the **Back Matter**, such as  *Endnotes*, *Copyright permissions*, *Glossary*, *Bibliography*, *Index*, and so on.

The Table of Contents and the navigators follow the lexicographical order, so `''` < `'dd'` < `'AX'` < `'BX'`, for instance.

For more information about the structure of a book, see [Parts of a Book Explained: Front Matter, Body, and Back Matter](https://blog.reedsy.com/front-matter-back-matter-book/).

## Usage

The two main functions in this module are

- `make_book()`: adds the Table of Contents, header, and navigators from the data provided in the arguments.
- `make_book_from_configfile()`: adds the Table of Contents, header, and navigators from the data stored in a YAML configuration file given as argument.
The latter function simply reads the parameters from the configuration file and passes them to the `make_book()` function.

The `make_book()` function calls the following functions in this module, which take care of each of the three main features of the bookmaker:

- `add_contents()`: adds the Table of Contents to a selected "Contents" file.
- `add_headers()`: adds a header to each notebook with a given book info.
- `add_navigators()`: adds navigation bars to the top and bottom of each notebook.

Each of these later three functions can be called separately, if only one of the features is desired.

When running `jupyterbookmaker.py` as a script, it expects the filename of the configuration file and calls the function `make_book_from_configfile(config_file)`, where config_file is the name of the configuration file.

Look at the documentation for more information on each of these functions and for the other functions available on this package.

## Example

The most convenient way to use the module, or script, is via a configuration file. Say we have a configuration file called `config.yml`, in the same directory as the notebooks, and with the following content:

```yaml
book:
  toc_nb_name: 00.00-Front_Page.ipynb
  header: "*[Header for the notebooks in the jupyterbookmaker module](https://github.com/rmsrosa/jupyterbookmaker)*"
  core_navigators:
    - 00.00-Front_Page.ipynb
    - BA.00-References.ipynb
  user: rmsrosa
  repository: jupyterbookmaker
  branch: master
  github_nb_dir: tests/notebooks
  show_colab: True
  show_binder: True
  show_full_entry_in_nav: False
```

Then, we import the module (in the same folder) and use the `make_book()` method with this configuration file as argument:

```python
import jupyterbookmaker as jbm
jbm.make_book('config.yml')
```

Or we execute it as a script in the command line:

```bash
./jupyterbookmaker.py config.yml
```

If we call the `jbm.make_book('config.yml')` from a different directory, we should add the parameter `directory` to the configuration file, with the path to the collection of notebooks.

## Colab and Binder links

Notice, in the example configuration file above, the parameters `show_colab: True` and `show_binder: True`, and other parameters with the information about the github repository and directory where the notebooks in this package reside. This allows the module to add direct links for the corresponding notebooks to be opened in one of this cloud computing python environments.

When opening the direct links from within the notebook rendering of the github, it is necessary to click with the right button, otherwise nothing will be opened.

## Further examples

See more examples in the `tests` directory:

- There are five examples of configuration files in the `tests` subdirectory [config1.yml](tests/config1.yml), [config2.yml](tests/config2.yml), [config3.yml](tests/config3.yml), [config4.yml](tests/config4.yml), [config5.yml](tests/config5.yml). Have a look a them for examples of different configuration parameters.
- To run one of the examples, go to `bash` terminal at the `tests` subdirectory and run

  ```bash
  ../jupyterbookmaker/jupyterbookmaker.py config1.yml
  ```

or any of the other config files. This runs the `jupyterbookmaker.py` as a script.

- An example of using `jupyterbookmaker` as a module is in `/tests/makebook_test.py`
- One can also use the module from inside a jupyter notebook. This is show in both collections of notebooks in the `notebooks` and `lectures` folders. This is, in fact, the most convenient way.

In the first examples, the script is ran from the directory `tests`, while the notebooks are the subdirectory `notebooks`. In this case, the following lines should be added to the configuration file, so the script knowns where to find the notebooks:

```yaml
directory:
  app_to_notes_path: notebooks
```

## Requirements

It uses the following standard libraries:

- [re](https:/docs.python.org/3/library/re.html)
- [os](https:/docs.python.org/3/library/os.html)
- [itertools](https:/docs.python.org/3/library/itertools.html)
- [sys](https:/docs.python.org/3/library/sys.html)

Besides the libraries in the standard implementation, it requires the `nbformat` module, to interact with the jupyter notebooks, and the `yaml` package, to read `*.yml` configuration files:

- [nbformat](https://pypi.org/project/nbformat/),
- [yaml](https:/docs.python.org/3/library/yaml.html).

## Credits

This package is based on the three modules present, in early 2018, in the subdirectory [`tools`](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/tools) of the [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook), by [Jake VanderPlas](http://vanderplas.com/).

## License

The original work in [Python Data Science Handbook/tools](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/tools) is licensed by [Jake VanderPlas](http://vanderplas.com/) under the [MIT license](https://opensource.org/licenses/MIT).

The current modifications in this package is now being license as well under the [MIT license](https://opensource.org/licenses/MIT). See the file [LICENSE](LICENSE).
