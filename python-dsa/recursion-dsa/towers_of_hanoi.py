def ToH(n_disks, sp=1, ep=3):
    if (n_disks):
        ToH(n_disks-1, sp, 6-sp-ep)
        print(f"Moving disk{n_disks} from {sp} to {ep}")
        ToH(n_disks-1, 6-sp-ep, ep)

ToH(3)