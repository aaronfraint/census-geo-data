from numpy import save
import pandas as pd
from pathlib import Path

from census_geo_data.get_shapes import get_tiger_shapes
from census_geo_data.get_table import get_api_table


def save_shapefile(
    table_id: str = "B08301",
    year: int = 2019,
    geo: str = "TRACT",
    state_fips: int = 42,
    data_dir: str = None,
) -> None:
    """
    Get geo and tabular data, join them together
    """

    # Get raw data from census
    gdf = get_tiger_shapes(year, geo, state_fips)
    df = get_api_table(table_id, year, geo, state_fips)

    gdf.to_crs(epsg=4326, inplace=True)

    joined_gdf = pd.concat([gdf, df], axis=1)

    filename = f"acs5_{year}_{table_id}_{geo.lower()}_in_state_{state_fips}.shp"

    if not data_dir:
        output_file = Path.cwd() / filename
    else:
        output_file = Path(data_dir) / filename

    joined_gdf.to_file(output_file)


if __name__ == "__main__":
    save_shapefile(
        data_dir="/Volumes/GoogleDrive/Shared drives/U_City_FY_21/ExistingConditions/Census Data"
    )
