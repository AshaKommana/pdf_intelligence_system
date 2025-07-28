# Connecting the Dots - Round 1B

This project extracts and ranks relevant document sections based on a user persona and task.

## How to Use

1. Put 3–10 PDFs inside the `input/` folder.
2. Edit `persona.json` with the given persona and task.
3. Build and run the Docker image.

## Docker Commands

### Build
```
docker build --platform linux/amd64 -t pdfintelligence:latest .
```

### Run
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdfintelligence:latest
```

## Output
You will get `intelligent_output.json` in the `output/` folder.