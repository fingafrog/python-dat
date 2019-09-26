[![codebeat badge](https://codebeat.co/badges/69998b54-da96-4a48-ac50-835eac0beeb1)](https://codebeat.co/projects/github-com-christopherpryer-dat-python-master)

# dat-python
Python package for Dat Rateview http session manipulation.

### Functionality
- search_locations: get a location handle from dat. This maps to a best-guess
id for a location search. Searches are strings in the format
'city, state, zip'.
- search_historicals: get json of historical market data for a origin-handle
to dest-handle search.
- search: search Dat Rateview using origin, destination, and equipment strings.

### Instructions
Searching Dat RateView using PandasWrapper helper:


```python
from dat.helpers import PandasWrapper
username = 'dat username here'
password = 'dat password here' # NOTE: it's recommended to use os.environ
token = {'userName': username, 'password': password}
helper = PandasWrapper(token)

origin = 'Cherry Hill, NJ, 08002'
destination = 'Philadelphia, PA, 19106'
df = helper.search(origin, destination, equipment='Dry')
```
