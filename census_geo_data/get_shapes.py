import geopandas as gpd


def get_tiger_shapes(
    year: int = 2019, geo: str = "TRACT", state_fips: int = 34
) -> gpd.GeoDataFrame:
    """
    Load TIGER shapefile from Census' FTP page into a geodataframe
    """

    _supported_types = ["TRACT"]

    geo = geo.upper()

    if geo.upper() not in _supported_types:
        print("This TIGER geometry type is not yet supported.")
        return None

    url = f"https://www2.census.gov/geo/tiger/TIGER{year}/{geo.upper()}/tl_{year}_{state_fips}_{geo.lower()}.zip"
    gdf = gpd.read_file(url)

    return gdf
