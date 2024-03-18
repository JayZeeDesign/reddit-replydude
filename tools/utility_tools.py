import time
from langchain.tools import tool


class UtilityTools:

    @tool("Wait for certain amount of time")
    def wait(mins):
        """Wait for certain amount of time"""
        duration_in_seconds = mins * 60
        time.sleep(duration_in_seconds)

        print(f"great, you've waitted {mins} mins! now proceed your task")
        return f"great, you've waitted {mins} mins! now proceed your task"
