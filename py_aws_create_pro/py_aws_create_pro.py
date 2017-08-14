import boto3


def main():
    py_aws_create_pro('InstanceSecurityGroup', 'Enable SSH access',
                      'tcp', '22', '22', '0.0.0.0/0', 'vpc-8fbd60e9')


def py_aws_create_pro(sg_name, sg_desc, sg_ingress_IpProtocol, sg_ingress_FromPort, sg_ingress_ToPort, sg_ingress_CidrIp, VpcId):
    ec2_client.create_security_group(sg_name, sg_desc, sg_ingress_IpProtocol,
                                     sg_ingress_FromPort, sg_ingress_ToPort, sg_ingress_CidrIp, VpcId)


ec2_client = boto3.client("ec2")

if __name__ == "__main__":
    main()
