# SyncStream

SyncStream is a Python program designed to facilitate the synchronization of streaming media across networked Windows devices, ensuring a seamless viewing experience. It supports both server and client roles for managing and receiving synchronization commands.

## Features

- Simple server-client architecture.
- Broadcast synchronization messages to all connected clients.
- Easy setup for both server and client.

## Requirements

- Python 3.x
- Windows operating system

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/syncstream.git
cd syncstream
```

## Usage

### Server

To start the server, run:

```bash
python syncstream.py server
```

The server will listen for incoming client connections on the default port (`12345`).

### Client

To start a client, run:

```bash
python syncstream.py client [server_ip]
```

Replace `[server_ip]` with the IP address of the server.

## Example

1. Start the server on one device:

   ```bash
   python syncstream.py server
   ```

2. Connect a client from another device:

   ```bash
   python syncstream.py client 192.168.1.10
   ```

   Replace `192.168.1.10` with the actual IP address of the server.

3. The client will receive synchronization messages and display them in the terminal.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.