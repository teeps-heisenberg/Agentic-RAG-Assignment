"""
Helper script to set up environment
Run this to create your .env file
"""

import os


def setup_env():
    """Interactive setup for environment variables"""
    print("=" * 60)
    print("  ENVIRONMENT SETUP")
    print("=" * 60)
    print("\nThis will create a .env file with your Gemini API key.")
    print("Get your API key from: https://makersuite.google.com/app/apikey\n")
    
    api_key = input("Enter your Gemini API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Setup cancelled.")
        return
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(f"GEMINI_API_KEY={api_key}\n")
    
    print("\n✅ Environment file created successfully!")
    print("You can now run: python main.py")


if __name__ == "__main__":
    setup_env()
