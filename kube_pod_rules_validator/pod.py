from kubernetes import client, config


class Pod(object):

    def __init__(self, name, image, labels, recent_start_time=None):
        self.name = name
        self.images = image
        self.labels = labels
        self.recent_start_time = recent_start_time


class PodApi(object):

    def __init__(self):
        config.load_kube_config()
        v1 = client.CoreV1Api()
        self.pods = v1.list_pod_for_all_namespaces(watch=False)

    def __get_images(self, pod):
        images = []
        for container in pod.item.spec.containers:
            images.append(container.image)
        return images

    def __get_labels(self, pod):
        return pod.metadata.labels

    def build_pod_details(self):
        pod_details = []
        for pod in self.pods.items:
            name = pod.metadata.name
            images = self.__get_images(pod=pod)
            labels = self.__get_labels(pod=pod)
            pod_details.append(
                Pod(
                    name=name,
                    images=images,
                    labels=labels
                )
            )
        return pod_details

