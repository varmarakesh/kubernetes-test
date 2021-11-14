from kube_pod_rules_validator.pod import PodApi
from kube_pod_rules_validator.rules import ApplyRules
import pprint


def main():
    pod_api = PodApi()
    pods = pod_api.build_pod_details()
    rules = ApplyRules()
    result = rules.validate(
        pods=pods
    )
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)


# start of projection execution
if __name__ == '__main__':
    main()
