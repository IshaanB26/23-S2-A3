from island import Island

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = islands
        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_islands = []
        for island in self.islands:
            if island.marines > 0:
                pirates_to_send = min(self.crew, island.marines)
                money_earned = min(pirates_to_send * island.money/ island.marines, island.money)
                selected_islands.append ((island, pirates_to_send))
                self.crew -= pirates_to_send
        return selected_islands

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        money_earned_list = []
        for crew_count in crew_numbers:
            self.crew = crew_count
            total_money_earned = sum(min(pirates_to_send * island.money /island.marines, island.money)
                                     for island, pirates_to_send in self.select_islands())
            money_earned_list.append (total_money_append)
        return money_earned_list

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        island.money = new_money
        island.marines = new_marines
