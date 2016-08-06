# Name-Detector

## How to run the docker container:
- Clone and extract the repository. 
- Open terminal in the directory inside the extracted folder the extracted.
- Build the docker image by running this command:
    ```sh
    docker-compose build
    ```
- After building the image, you can run the python detector by running this command:
    ```sh
    docker-compose up
    ```
    This will run the python script where it first shows the result of the 3 sample text files stored in folder "samples". Then, you can type a text on the terminal and it will show the output of the given text.  
    
## Example:
#### Input:
```
Donald Trump had a meeting with Vladimir Putin yesterday. There were drinking vodka and visiting banya all night long. Alexander Lukashenko was offended that he was not in a party.
```
#### Output:
```
List of person names: ['Donald Trump', 'Alexander Lukashenko', 'Vladimir Putin']
```
