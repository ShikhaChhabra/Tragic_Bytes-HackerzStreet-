import pymysql
from datetime import date
from test_Npcap import get_mac_addresses

# Function to mark attendance in the database
def mark_attendance(student_id, status):
    # Connect to the MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='@Ironman0107#',
        database='hack'
    )
    cursor = conn.cursor()
    
    # Insert attendance record
    cursor.execute("INSERT INTO attendence (Reg_no, date, status) VALUES (%s, %s, %s)", (student_id, date.today(), status))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Get the MAC addresses obtained from the script
ip_range = "192.168.21.0/24"  # Specify the IP range of your network
devices = get_mac_addresses(ip_range)
script_mac_addresses = [device['mac'] for device in devices]

# Connect to the MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='@Ironman0107#',
    database='hack'
)
cursor = conn.cursor()

# Compare MAC addresses with database and mark attendance
for mac_address in script_mac_addresses:
    # Query database for student with matching MAC address
    cursor.execute("SELECT Reg_no FROM students WHERE MAC=%s", (mac_address,))
    result = cursor.fetchone()
    if result:
        student_id = result[0]
        mark_attendance(student_id, 'present')
    else:
        cursor.execute("SELECT Reg_no FROM students WHERE MAC=%s", (mac_address,))
        result = cursor.fetchone()
        student_id = result[0]
        mark_attendance(student_id, 'absent')
        # print("Unknown MAC Address:", mac_address)
        
# Close the database connection
conn.close()
