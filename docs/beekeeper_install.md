# Beekeeper Studio Installation Guide

Beekeeper Studio is an open-source SQL editor that works on Windows, macOS, and
Linux. These steps walk an interviewee through installation so they can browse
the assessment database without relying solely on CLI tooling.

## 1. Download the Installer

- Navigate to <https://www.beekeeperstudio.io/get>
- Choose the installer that matches your operating system:
  - **Windows:** `.exe` installer (works on Windows 10/11)
  - **macOS:** `.dmg` (Apple Silicon and Intel builds are provided)
  - **Linux:** AppImage, Snap, Flatpak, or `.deb` / `.rpm`

## 2. Install

- **Windows:** run the `.exe`, follow the wizard, keep the default options.
- **macOS:** open the `.dmg`, drag Beekeeper Studio into `Applications`.
- **Linux:** use your package manager (e.g. `sudo apt install ./beekeeper.deb`)
  or make the AppImage executable (`chmod +x Beekeeper-Studio.AppImage`).

## 3. Launch & Sign In (optional)

Start Beekeeper Studio after installation. The free community edition works
without creating an account, so you can skip the sign-in prompt if desired.

## 4. Prepare Database Credentials

Collect the same connection information used by the FastAPI application:

- Hostname / endpoint (e.g., `your-db.cluster-xyz.us-east-1.rds.amazonaws.com`)
- Port (default `3306`)
- Username and password
- Database/schema name (from `MYSQL_DB`)

You can store these values in your `.env` file and copy them when setting up
Beekeeper Studio.

Once installed, follow `docs/beekeeper_view_data.md` to connect and inspect the
tables.

