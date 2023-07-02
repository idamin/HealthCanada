# Drug Product Database Optimization

This script is a side project that I undertook during my time as an Intern for the Pricing Analytics team at Apotex.
As a feasibility test, this project was meant for me to experiment with the DPD API in order to automate manual daily tasks. Therefore, this is a bare-bones version of the working script.

The purpose of the script is as follows:
Given a list of Drug Identification Numbers (DINS) in an Excel file, extract the Company, Product Name, Status, and Schedule of the Drug from the DPD API, and present that information as a table in the same Excel file.

Originally using the Health Canada API, the API was not maintained, as such the switch to the DPD API was made.

```
Health Canada API:
https://node.hres.ca/docs.html#drug-product-docs

DPD API:
https://health-products.canada.ca/api/documentation/dpd-documentation-en.html
```
