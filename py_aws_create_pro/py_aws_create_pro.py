import boto3


def main():
    create_sg(sg_name='InstanceSecurityGroup5', sg_desc='Enable SSH access', sg_ingress_IpProtocol='tcp',
              sg_ingress_FromPort=22, sg_ingress_ToPort=22, sg_ingress_CidrIp='0.0.0.0/0', VpcId='vpc-8fbd60e9')


ec2 = boto3.client('ec2')


def create_sg(**kwargs):
    response = ec2.create_security_group(
        GroupName=kwargs['sg_name'], Description=kwargs['sg_desc'], VpcId=kwargs['VpcId'])
    ec2.authorize_security_group_ingress(GroupId=response['GroupId'], IpProtocol=kwargs['sg_ingress_IpProtocol'], CidrIp=kwargs["sg_ingress_CidrIp"], FromPort=kwargs["sg_ingress_FromPort"],
                                         ToPort=kwargs['sg_ingress_ToPort'])


if __name__ == '__main__':
    main()
