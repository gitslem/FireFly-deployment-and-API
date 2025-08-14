# FireFly 

## Files Included
- `Todo.sol`: Ethereum smart contract for the Todo app.
- `app.py`: Gradio front-end to interact with the FireFly HTTP API.

## Usage Instructions

### 1. Run FireFly Node
```bash
firefly new -n firefly_assignment2 -o SaberOrg1,SaberOrg2,SaberOrg3 -m simple
cd firefly_assignment2
firefly start
```

### 2. Deploy Smart Contract using FFI
Use FireFly UI or API to create an FFI interface using the ABI of `Todo.sol`.

### 3. Launch Gradio App
```bash
pip install gradio requests
python app.py
```

Ensure the FireFly node is running and the smart contract is deployed via FFI with the name `todo_contract`.

### 4. API Examples
See the main documentation or refer to the provided curl commands in your terminal.
