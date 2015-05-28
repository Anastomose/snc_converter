.. netcdf_csv documentation master file, created by
   sphinx-quickstart on Tue Apr 14 18:27:22 2015.

======================================
netcdf_csv Documentation
======================================

Table of Contents:
-------------------

* :ref:`start_of_readme`
* :doc:`Datasets`
* :doc:`Variables`
* :doc:`Resources`

.. _start_of_readme:

Readme
------

netcdf_csv is being developed as a tool to move data between the netcdf format that is preferred by for data storage and archiving and the more user-friendly tab-separated value that allows users to examine data using spreadsheets.

netcdf_csv is a python module that will allow for quick conversion of a formatted spreadsheet into netcdf format using the netcdf_csv API. netcdf_csv will also allow for dumping of netcdf files into a formatted spreadsheet through the netcdf_csv API.

Current Status
----------------

netcdf_csv can now instantiate a new dataset from a formatted TSV file including variables, dimensions, and global attributes. Fill values are not currently loading into the dataset.

Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
