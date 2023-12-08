import os
import sys

def extract_nrio_data(data_path, bank_data):
    with open(data_path, "rb") as f:
        dump_data = f.read()

    output_dir = "extracted_data"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Now extracting ...\n")

    for bank_name, start_offset, end_offset in sorted(bank_data, key=lambda x: x[1]):
        bank_size = end_offset - start_offset
        bank_data = dump_data[start_offset : end_offset]

        output_filename = f"{output_dir}/{bank_name}"
        with open(output_filename, "wb") as bank_file:
            bank_file.write(bank_data)

        print(f"Extracted {bank_name} (Size: {bank_size // 1024} KB) to {output_filename}")

    total_size = len(dump_data)
    print(f"Total image size: {total_size // 1024} KB")


# Usage: python3 extract_nrio_data.py nrio_data.bin
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("extract_nrio_data v0.1 by SylverReZ")
        print("extracts banks from an 'nrio_data.bin' file dump using nrioTool.\n")
        print("Usage: python3 extract_nrio_data.py <nrio_data.bin>")
        sys.exit(1)

    data_path = sys.argv[1]

    # Bank data: [Bank Name, Start Offset, End Offset]
    bank_data = [
        ["init_data.bin", 0x0000000, 0x00003FF],  # (possibly init data for ASIC?)
        ["stage1.nds", 0x0000400, 0x0002FFF],  # Stage-1 (primary ROM)
        ["stage1_index.bin", 0x0008000, 0x0017FFF],  # Stage-1 (primary) index table
        ["stage2.nds", 0x0020000, 0x0034FFF],   # Stage-2 (secondary ROM)
        ["stage2_index.bin", 0x0040000, 0x007FFFF],   # Stage-2 (secondary) index table - nulled on bootlegs
        ["udisk.nds", 0x0080000, 0x011223F],   # uDisk binary (i.e., uDisk v1.45 = 0x9223F in size) - please change the offsets for older versions
        #["game.nds", 0x0040000, 0x08AFFFF],   # Full retail ROM dump (if flashed in 'no-menu mode')
        ["nrio_fat_image.img", 0x08B0000, 0x7FFFFFF]   # Stage-2 (secondary ROM) - specify the end offset for your size of cart
    ]

    extract_nrio_data(data_path, bank_data)
