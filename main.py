from kube_pod_rules_validator.pod import Pod
from kube_pod_rules_validator.rules import Rules


def main():
    pod = Pod()
    images = pod.get_images()
    rules = Rules()
    print(rules.validate(images=images))


# start of projection execution
if __name__ == '__main__':
    main()
