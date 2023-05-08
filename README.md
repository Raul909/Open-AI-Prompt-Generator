
# OpenAI Web Application


The OpenAI Web Application is a simple interface for generating responses using the OpenAI API's GPT-3 language model. Users can input a prompt and receive a response generated by the OpenAI API.




## Installation

To install and run the web application, follow these steps:

1.Clone the repository from GitHub: git clone https://github.com/Raul909/Open-AI-Prompt-Generator.git

2.Install the required Python packages: pip install -r requirements.txt

3.Create a file named .env in the project directory and set the OPENAI_API_KEY environment variable to your OpenAI API key: OPENAI_API_KEY=<your-api-key>

4.Run the application: python app.py
Navigate to http://localhost:5000 in your web browser to access the home page.
    
## Usage

The home page of the web application displays a simple welcome message and an input field for the user to enter a prompt. Once the prompt is entered, the user can click the "Generate" button to submit the prompt and receive a response generated by the OpenAI API.


## API Documentation

The web application provides a simple API for generating responses using the OpenAI API.


## API Reference

#### Request Parameters



| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `prompt` | `string` | The prompt to generate a response for. |

#### Response

On success, the API will return a JSON object with the following fields:

| Field | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `message`      | `string` | The response generated by the OpenAI API in response to the provided prompt. |




## Example

Request

![App Screenshot](https://github.com/Raul909/Open-AI-Prompt-Generator/blob/main/screenshots/Screenshot%202023-05-08%20220835.png)

Response

![App Screenshot](https://github.com/Raul909/Open-AI-Prompt-Generator/blob/main/screenshots/Screenshot%202023-05-08%20220947.png)



## Contributing

Contributions to the OpenAI Web Application are welcome! If you would like to contribute, please fork the repository and submit a pull request


## License

The OpenAI Web Application is released under the [MIT License](https://choosealicense.com/licenses/mit/).

