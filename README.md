# URL Shortener

A simple Python script to shorten URLs using the Cutt.ly API. This script takes a full-length URL and a desired name for the shortened link and then makes a request to the Cutt.ly API to generate a shortened URL.

## Prerequisites

Before running the script, you'll need to have the following:

- Python 3 installed on your system.
- The `requests` library. You can install it using the following command:

```bash
pip install requests
```

## Getting Started

1. Clone the repository or download the script directly.

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Open the terminal or command prompt and navigate to the directory where the script is located.

```bash
cd path/to/your-repo
```

3. Run the script by providing a full-length URL and a desired name for the shortened link.

```bash
python shorten_link.py
```

## Usage

In the terminal or command prompt, you will be prompted to enter a full-length URL and a name for the shortened link. The script will then make a request to the Cutt.ly API to generate the shortened URL. If successful, the script will display the title and the shortened link.

## API Key

To use the Cutt.ly API, you need to have an API key. If you don't have one, you can sign up for a free account at [https://cutt.ly](https://cutt.ly). Once you have the API key, replace the `API_KEY` variable in the `shorten_link.py` script with your actual API key.

## Error Handling

The script provides error handling for various scenarios that might occur while generating the shortened URL:

- If the link has already been shortened by the Cutt.ly domain.
- If the entered link is not a valid URL.
- If the preferred link name is already taken.
- If the API key is invalid.
- If the link includes invalid characters.
- If the link is from a blocked domain.
- If you have reached your monthly link limit.

In case of any error, the script will display an appropriate error message.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this code as per the terms of the MIT License. However, please note that this project comes with no warranty or support.

## Acknowledgments

- This script uses the Cutt.ly API to shorten URLs. Visit their website at [https://cutt.ly](https://cutt.ly) for more information about their service.

Please ensure you comply with the Cutt.ly API usage policy while using this script.
