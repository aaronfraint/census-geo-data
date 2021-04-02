import requests
import pandas as pd


def get_api_table(
    table_id: str = "B08301", year: int = 2019, geo: str = "TRACT", state_fips: int = 34
) -> pd.DataFrame:
    """
    Get tabular data from the Census API as a dataframe
    """

    url = f"https://api.census.gov/data/{year}/acs/acs5"

    params = {
        "get": f"group({table_id})",
        "for": f"{geo.lower()}:*",
        "in": f"state:{state_fips}",
        # "key": None,
    }

    sesh = requests.session()
    response = sesh.get(url, params=params)
    data = response.json()

    headers = data.pop(0)
    df = pd.DataFrame(data=data, columns=headers)

    # Make column names less verbose
    # ... turning 'B08301_001E' into 'c_001e'
    df.columns = df.columns.str.replace(table_id, "c")
    df.columns = df.columns.str.lower()

    # Drop columns full of null values
    df.dropna(axis=1, inplace=True)

    # Strip out the national identifier of the geoid to facilitate joining to shapefile
    df["geo_join"] = df["geo_id"].str.replace("1400000US", "")

    return df


if __name__ == "__main__":
    df = get_api_table()