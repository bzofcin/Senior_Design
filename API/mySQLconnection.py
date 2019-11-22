import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='unlvteamseven', ssh_password='Unlv#2019',
    remote_bind_address=('unlvteamseven.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='unlvteamseven', password='Team7MySQL',
        host='127.0.0.1', port=3306,
        database='unlvteamseven$aistockpickerdb',
    )
    # Do stuff
    connection.close()