import tv
def main():
    my_tv = tv.TV()
    my_tv.set_channel(1)
    print(my_tv.show_status())
    my_tv.turn_on()
    print(f"Channels: {my_tv.channels}")
    my_tv.set_channel(2)
    print(my_tv.show_status())
    my_tv.turn_off()
if __name__ == "__main__":
    main()