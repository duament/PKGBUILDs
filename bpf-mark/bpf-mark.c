#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

SEC("cgroup/sock")
int bpf_prog1(struct bpf_sock *sk) {
	sk->mark |= 0x1;
	return 1;
}

char _license[] SEC("license") = "GPL";
