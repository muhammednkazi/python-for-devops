instance_type=input("Enter Instance Type:-\n")


if instance_type == "t2.micro":
    print("Instance will be created")
elif instance_type == "t2.medium":
    print("Instance will be created")
else:
    print("Invalid instance")