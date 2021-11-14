from kube_pod_rules_validator.pod import PodApi
from kube_pod_rules_validator.rules import Rules


def main():
    pod_api = PodApi()
    pods = pod_api.build_pod_details()
    rules = Rules()
    result = rules.validate(
        pods=pods
    )
    print(result)


# start of projection execution
if __name__ == '__main__':
    main()
