from kubernetes import client, config


class Pod(object):

    def __init__(self):
        config.load_kube_config()
        v1 = client.CoreV1Api()
        self.pods = v1.list_pod_for_all_namespaces(watch=False)

    def get_images(self):
        images = []
        for item in self.pods.items:
            for container in item.spec.containers:
                images.append(container.image)
        return images

    def get_labels(self):
        return []
