from common.common_consts import zero_trust_consts
from common.common_consts.zero_trust_consts import NETWORKS
from monkey_island.cc.services.zero_trust.scoutsuite.consts.ec2_rules import EC2Rules


class PERMISSIVE_FIREWALL_RULES:
    rules = [EC2Rules.SECURITY_GROUP_ALL_PORTS_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_TCP_PORT_TO_ALL,
             EC2Rules.SECURITY_GROUP_OPENS_UDP_PORT_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_RDP_PORT_TO_ALL,
             EC2Rules.SECURITY_GROUP_OPENS_SSH_PORT_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_MYSQL_PORT_TO_ALL,
             EC2Rules.SECURITY_GROUP_OPENS_MSSQL_PORT_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_MONGODB_PORT_TO_ALL,
             EC2Rules.SECURITY_GROUP_OPENS_ORACLE_DB_PORT_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_POSTGRESQL_PORT_TO_ALL,
             EC2Rules.SECURITY_GROUP_OPENS_NFS_PORT_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_SMTP_PORT_TO_ALL,
             EC2Rules.SECURITY_GROUP_OPENS_DNS_PORT_TO_ALL, EC2Rules.SECURITY_GROUP_OPENS_ALL_PORTS_TO_SELF,
             EC2Rules.SECURITY_GROUP_OPENS_ALL_PORTS, EC2Rules.SECURITY_GROUP_OPENS_PLAINTEXT_PORT_FTP,
             EC2Rules.SECURITY_GROUP_OPENS_PLAINTEXT_PORT_TELNET, EC2Rules.SECURITY_GROUP_OPENS_PORT_RANGE]

    pillars = [NETWORKS]

    test = zero_trust_consts.TEST_SCOUTSUITE_PERMISSIVE_FIREWALL_RULES
