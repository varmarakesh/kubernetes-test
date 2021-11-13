from kube_pod_rules_validator.pod import Pod


def main():
    pod = Pod()
    print(pod.get_images())


# start of projection execution
if __name__ == '__main__':
    main()
