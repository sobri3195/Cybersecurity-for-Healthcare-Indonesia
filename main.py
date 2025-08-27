import argparse
from utils.scanner import scan_host

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pemindai Keamanan Siber untuk Sistem Kesehatan Indonesia")
    parser.add_argument("--target", required=True, help="IP target untuk dipindai (contoh: 192.168.1.100)")
    args = parser.parse_args()

    scan_host(args.target)
