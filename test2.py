# Import the snowflake connector module
import sys
import snowflake.connector

# main section 

sfk_user = sys.argv[1]
sfk_password = sys.argv[2]
sfk_account = sys.argv[3]
sfk_role = sys.argv[4]
sfk_warehouse_name = sys.argv[5]
sfk_warehouse_size = sys.argv[6]
# sfk_min_clusters = sys.argv[7]
# sfk_max_clusters = sys.argv[8]
# sfk_auto_resume = sys.argv[7]
# sfk_auto_suspend = sys.argv[8]
# sfk_scaling_policy = sys.argv[9]
# sfk_warehouse_type = sys.argv[10]


print("PY:--- Main Warehouse script Starts ")
#sfk_user,sfk_password,sfk_account,sfk_role,sfk_warehouse_name,sfk_warehouse_size,sfk_min_clusters,sfk_max_clusters,sfk_auto_resume,sfk_auto_suspend,sfk_scaling_policy,sfk_warehouse_type = sys.argv[1:]
#sfk_user,sfk_password,sfk_account,sfk_role,sfk_warehouse_name = sys.argv[1:]
#print("PY:--- sys.argvs --->",sfk_user,sfk_password,sfk_account,sfk_role,sfk_warehouse_name,sfk_warehouse_size,sfk_min_clusters,sfk_max_clusters,sfk_auto_resume,sfk_auto_suspend,sfk_scaling_policy,sfk_warehouse_type,"\n",sep="\nPY:--- sys.argv --->")
#print("PY:--- sys.argvs --->",sfk_user,sfk_password,sfk_account,sfk_role,sfk_warehouse_name,"\n",sep="\nPY:--- sys.argv --->")

# Create a SQL statement to create the warehouse
sfk_create_update_sql_command = f"CREATE WAREHOUSE IF NOT EXISTS {sfk_warehouse_name } WITH WAREHOUSE_SIZE= '{sfk_warehouse_size}';"

sfk_validate_sql_command = " SHOW WAREHOUSES LIKE '" + sfk_warehouse_name +"'"
# sfk_remove_sql_command = " DROP WAREHOUSE IF EXISTS GDP_AUTOMATION_TEST_CHECK "  


# Connect to Snowflake
connection = snowflake.connector.connect(
    user=sfk_user,
    password=sfk_password,
    account=sfk_account,
    role=sfk_role
)


try:
    # Create a cursor object
    cursor = connection.cursor()
    # Create the warehouse
    cursor.execute(sfk_create_update_sql_command)

    # Show the warehouse details
    # cursor.execute(f"SHOW WAREHOUSES LIKE '{sfk_warehouse_name}'")
    print("PY:--- Validate command : ",sfk_validate_sql_command)
    cursor.execute(sfk_validate_sql_command)
    result = cursor.fetchall()
    print(result)

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("PY:--- Completed successfully - Warehouse script \n")
except Exception as ex:
    print("PY:--- Exception at python execution 'warehouse creation' ",ex,"\n")
    sys.exit(1)