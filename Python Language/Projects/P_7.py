
# import time

# from pip._internal.cli.progress_bars import get_download_progress_renderer


# if __name__ == "__main__":
#     chunks = []
#     b = get_download_progress_renderer(bar_type="on",size=100)
#     for i in range(100):
#         chunks.append(range(i))
#         for bb in b(chunks):
#             time.sleep(.1)


# import time 
# from rich.progress import track
# load=50
# for n in track(range(load), description="Processing..."):
#     time.sleep(n)
#     print(n)

list=[1,2,3,4,5,6,7,8,9,10]

list1=[i**3 for i in list ]

print(list1)


