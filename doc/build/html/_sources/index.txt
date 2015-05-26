.. netcdf_csv documentation master file, created by
   sphinx-quickstart on Tue Apr 14 18:27:22 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

======================================
Welcome to netcdf_csv's Documentation
======================================

Table of Contents:

.. toctree::
   :maxdepth: 1

   Datasets
   Variables
   Resources

.. _start_of_readme:

Readme
------

netcdf_csv is being developed as a tool to move data between the netcdf format that is preferred by for data storage and archiving and the more user-friendly tab-separated value that allows users to examine data using spreadsheets.

Climate research data is primarily stored and handled on the data management side using the netcdf format because it provides good metadata as well as a standard format to store and handle data in.

However, this format is not particularly user friendly to people performing climate analysis who primarily want to look at the data as a data series that can be dumped into a spreadsheet for plotting and other analysis. This usually means converting the netcdf data to a CSV or other character delimited format that can be read in Excel.

This project consists of building a module that will provide a set of tools that can convert data back and forth between netcdf and CSV formats while preserving or adding appropriate metadata.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
