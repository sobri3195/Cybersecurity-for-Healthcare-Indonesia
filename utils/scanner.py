import nmap
from config.settings import TARGET_PORTS, TIMEOUT
from .logger import log_info, log_warning, log_alert

def scan_host(target_ip):
    log_info(f"Memindai target: {target_ip}")
    nm = nmap.PortScanner()
    try:
        nm.scan(target_ip, ' '.join(map(str, TARGET_PORTS)), arguments=f'-T4 --open --host-timeout {TIMEOUT}s')
        for proto in nm[target_ip].all_protocols():
            ports = nm[target_ip][proto].keys()
            for port in ports:
                state = nm[target_ip][proto][port]['state']
                service = nm[target_ip][proto][port]['name']
                msg = f"Port {port} ({service.upper()}) terbuka"
                log_info(msg)
                if port == 22:
                    log_alert("Port 22 (SSH) terbuka - periksa akses")
                elif port == 3306 or port == 5432:
                    log_warning(f"Port database {port} terbuka - pastikan tidak terpapar internet")
    except Exception as e:
        log_warning(f"Scan gagal: {e}")
