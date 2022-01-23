## Example of how to use Face API with Azure Functions | Python

### Steps for run project

1. [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)

   Benefits

   - Create a function from a trigger and language-specific template.
   - Run the function locally.
   - Publish the project to Azure.

2. Create virtual enviroment

```bash
virtualenv venv
```

3. Activate

```bash
source ./venv/bin/activate
```

4. Install dependencies

```bash
pip3 install -r requirements.txt
```

5. Run server locally

```bash
func host start
```

### Endpoints

[GET] http://localhost:7071/api/draw

- Params
  - single: Image with a face
  - multiple: Image with a face or multiple

```bash
http://localhost:7071/api/draw?single=https://i.ibb.co/yVxyc09/ibai.jpg&multiple=https://i.ibb.co/2jG2VLm/ibai-friends.jpg
```

### Single

![single](https://i.ibb.co/yVxyc09/ibai.jpg)

### Multiple

![multiple](https://i.ibb.co/2jG2VLm/ibai-friends.jpg)

### Output

![output](https://i.ibb.co/3zmzVZD/draw.jpg)

[POST] http://localhost:7071/api/similar

- Body
  - single: Image with a face
  - multiple: Image with a face or multiple

```json
{
  "single": "https://i.ibb.co/yVxyc09/ibai.jpg",
  "multiple": "https://i.ibb.co/2jG2VLm/ibai-friends.jpg"
}
```

### Test with CURL

```bash
curl -d '{"single": "https://i.ibb.co/yVxyc09/ibai.jpg","multiple": "https://i.ibb.co/2jG2VLm/ibai-friends.jpg"}' -H "Content-Type: application/json" -X POST http://localhost:7071/api/similar
```

### Output

```json
{
  "similar": true,
  "message": "Similar Faces",
  "facesNumber": {
    "single": 1,
    "multiple": 3
  },
  "drawUrl": "http://localhost:7071/api/draw?single=https://i.ibb.co/yVxyc09/ibai.jpg&multiple=https://i.ibb.co/2jG2VLm/ibai-friends.jpg"
}
```

### If not similar

```json
{
  "similar": false,
  "message": "No similar faces found image.jpg",
  "facesNumber": {
    "single": 1,
    "multiple": 1
  },
  "drawUrl": ""
}
```
