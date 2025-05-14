# 🧠 Solana & Anchor Development Environment Setup Guide
**By Abukhassym Khydyrbayev | SE-2318 | Blockchain Assignment 3.3**

This guide walks you through setting up a complete development environment for building decentralized applications (dApps) on the **Solana blockchain** using the **Anchor framework**, one of the most popular tools for Solana smart contract development.

Whether you're new to Solana or just looking to get your local development environment set up quickly, this guide will help you configure everything from scratch.

## 📚 Table of Contents
1. Prerequisites
2. Step-by-Step Setup
3. Project Structure
4. How to Run the Project
5. Troubleshooting
6. Completion Checklist

## 🛠️ Prerequisites
Before proceeding with the setup, ensure you have the following installed:

| Requirement | Version | Installation |
|-------------|---------|-------------|
| **Rust** | 1.68+ | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs` |
| **Node.js** | 14.x+ | Use `nvm` or download from nodejs.org |
| **Solana CLI** | 1.10+ | `sh -c "$(curl -sSfL https://release.solana.com/v1.10.32/install)"` |

You can verify each installation by running:
```bash
rustc --version
node --version
solana --version
```

## 🚀 Step-by-Step Setup

### 1. Install Anchor CLI
Anchor is a framework that simplifies writing secure Solana programs.

Install it via Cargo:
```bash
cargo install --git https://github.com/coral-xyz/anchor anchor-cli --locked
```

Verify installation:
```bash
anchor --version
# Expected output: anchor-cli 0.25.0+
```

### 2. Configure Solana Local Validator
Set the default cluster to localhost:
```bash
solana config set --url localhost
```

Check configuration:
```bash
solana config get
# Should show Config File: ~/.config/solana/cli/config.yml
# and URL: http://localhost:8899
```

### 3. Create Project Directory
Create a working directory for your Solana project:
```bash
mkdir ~/my-anchor-project && cd ~/my-anchor-project
```

### 4. Initialize Anchor Project
Run the following command to create a new Anchor project:
```bash
anchor init
```

This will generate the following structure:
```
.
├── Anchor.toml # Project configuration
├── programs/   # Smart contracts written in Rust
├── apps/       # Frontend dApp code
└── tests/      # Program test scripts
```

### 5. Start Local Validator
In a **new terminal window**, start the Solana test validator:
```bash
solana-test-validator
```

Leave this running while developing and testing.

### 6. Build & Deploy Program
From your project root, build and deploy your program:
```bash
anchor build # Compiles your Solana program
anchor deploy # Deploys it to the local validator
```

The output will include the **Program ID**, which you'll need for interacting with your deployed contract.

### 7. Verify Deployment
Use the Program ID from the previous step to check the account details:
```bash
solana account <PROGRAM_ID>
```

Replace `<PROGRAM_ID>` with the actual ID returned after deployment.

### 8. Run Tests
Anchor comes with built-in support for testing smart contracts. Run tests located in the `tests/` directory:
```bash
anchor test
```

This will compile, deploy, and execute your test suite automatically.

## 🗂️ Project Structure
After initialization, your project will look like this:
```
my-anchor-project/
│
├── Anchor.toml  # Configuration for Anchor CLI
├── programs/    # Contains your Solana smart contracts
├── apps/        # Placeholder for frontend integration
├── tests/       # Test files for your smart contracts
└── target/      # Compiled binaries (auto-generated)
```

## ▶️ How to Run the Project
1. Open Terminal 1 and start the local validator:
```bash
solana-test-validator
```

2. In Terminal 2, navigate to your project:
```bash
cd ~/my-anchor-project
```

3. Build and deploy:
```bash
anchor build
anchor deploy
```

4. Run tests:
```bash
anchor test
```

That's it! You now have a fully functional Solana development environment powered by Anchor.

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **Dependency issues** | Clean cargo cache and rebuild:<br>```bash<br>rustup update<br>cargo clean<br>anchor build<br>``` |
| **Validator not connecting** | Make sure `solana-test-validator` is running in another terminal. |
| **Version mismatches** | Check versions:<br>```bash<br>rustc --version<br>solana --version<br>anchor --version<br>``` |

## ✅ Completion Checklist
- ✅ I have installed Rust  
- ✅ I have installed Node.js  
- ✅ I have installed the Solana CLI  
- ✅ I have configured the local validator  
- ✅ I have created an Anchor project  
- ✅ I have built and deployed the program  
- ✅ I have successfully run tests  

## 🎯 Conclusion
With this guide, you've successfully set up a full Solana development environment using the Anchor framework. You are now ready to begin writing and deploying smart contracts, building dApps, and exploring the world of high-performance blockchain development.

This foundation opens the door to more advanced topics such as:
- Writing custom Solana programs
- Building user interfaces with React and web3.js
- Interacting with wallets like Phantom
- Testing and debugging complex smart contracts
