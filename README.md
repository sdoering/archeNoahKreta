# Bentham (S2D 'Digital Checkup Tool')


## Description

It is a tool from the SinnerSchrader Data Team to evaluate web domains regarding their digital performance in multiple dimensions
* technical perforamcne
* seo performance
* social media performance
* analytics and tracking
* ...

It therefore uses different services/APIs to gather the relevant data and provide graphs and insights to be then used in presentations. 

## Outlook
In the long run it shall provide data for a dashboarding solution like Kibana or Grafana. So that we cann do continously monitoring of client sites. 
Also the idea of alerts is being actively explored. 


## Project Structure.


### Project Organization


    │
    ├── data/               <- The original, immutable data dump. 
    │
    ├── figures/            <- Figures saved by scripts or notebooks.
    │
    ├── notebooks/          <- Jupyter notebooks. Naming convention is 'IPY-S2D' followed by a short `-` delimited 
    │                         description, a number (for ordering), and the creator's initials,
    │                        e.g. `IPY-S2D-initial-data-exploration-01-sd`.
    │
    ├── output/             <- Manipulated data, logs, etc.
    │
    ├── tests/              <- Unit tests.
    │
    ├── bentham/		    <- Python module with source code of this project.
    │
    ├── environment.yml     <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── README.md           <- The top-level README for developers using this project.


--------


## Set up

Install the virtual environment with conda and activate it:

```bash
$ conda env create -f environment.yml
$ source activate bentham 
```

Install `bentham` in the virtual environment:

```bash
$ pip install --editable .
```
If there are notebooks in 'notebooks/'
Run Jupyter Notebook and open the notebooks in `notebooks/`:

```bash
$ jupyter notebook
```

## Links

[GT Metrics](https://gtmetrix.com)
[Jeff Knupp](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
[15 Website Speed Test Tools](https://www.keycdn.com/blog/website-speed-test-tools/)
[Pythonic __init__.py](http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html)


