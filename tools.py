from countryinfo import CountryInfo
import periodictable

# Tool used to get chemical element details when name is given
def get_element_info_by_name(element_name:str) -> dict:
    """
    Retrieves and prints details of a chemical element by its name.
    Args:
        element_name (str): The name of the element (e.g., "Hydrogen", "Iron").
    Returns:
        JSON response that provides details of specified element (name, number, symbol, mass).
    """
    element_name_lower = element_name.lower()
    # Find the element by name
    element = None
    for el in periodictable.elements:
        if el.name.lower() == element_name_lower:
            element = el
            break

    if element:
        return {"status": "success",
                    "element_name": element.name,
                    "element_number": element.number,
                    "element_symbol": element.symbol,
                    "element_atomic_mass": element.mass}
    else:
        return {
                "status": "error",
                "error_message": f"Element not present: {element_name}",
            }


# Tool used to get country details when name is given
def get_country_details(country_name:str) -> dict:
    """
    Retrieves and prints details of a chemical element by its name.
    Args:
        country_name (str): The name of the country (e.g., "Hydrogen", "Iron").
    Returns:
        JSON response that provides details of specified country (name, capital, language spoken, currency used and timezone).
    """
    country_name_lower = country_name.lower()
    # Find the element by name
    country = None
    country = CountryInfo(country_name_lower)
    if country:
        return {"status": "success",
                    "country_name": country_name_lower,
                    "country_capital": country.capital(),
                    "country_number": country. languages(),
                    "country_symbol": country.currencies(),
                    "country_atomic_mass": country.timezones()}
    else:
        return {
                "status": "error",
                "error_message": f"Country not present: {country_name_lower}",
            }