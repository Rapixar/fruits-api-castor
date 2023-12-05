Fruits API Documentation
Overview
The Fruits API provides a simple interface for managing a collection of fruits. It allows users to view a list of fruits, get details about a specific fruit, and add a new fruit to the collection.

Base URL
The base URL for accessing the Fruits API is [your base URL]. All the following endpoints should be appended to this base URL.

Endpoints
1. List All Fruits
URL: /fruits
Method: GET
Description: Retrieves a list of all fruits in the database.
Response: A JSON array of fruit objects. Each object contains id, name, and color.
2. Get a Specific Fruit
URL: /fruits/{fruit_id}
Method: GET
URL Parameters: fruit_id (required) - The unique identifier of the fruit.
Description: Fetches details of a specific fruit by its ID.
Response: A JSON object containing the id, name, and color of the fruit. Returns null if no fruit is found with the given ID.
3. Add a New Fruit
URL: /add-fruit
Method: POST
Body Parameters: A JSON object containing:
id (Integer, required): The unique identifier for the new fruit.
name (String, required): The name of the fruit.
color (String, required): The color of the fruit.
Description: Adds a new fruit to the database.
Response: The newly created fruit object as a JSON.
Models
Fruit
id (Integer): A unique identifier for the fruit.
name (String): The name of the fruit.
color (String): The color of the fruit.
Errors
The API uses conventional HTTP response codes to indicate success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error due to the provided information (e.g., a required parameter was missing, a fruit with the given ID was not found, etc.), and codes in the 5xx range indicate an error with the server.