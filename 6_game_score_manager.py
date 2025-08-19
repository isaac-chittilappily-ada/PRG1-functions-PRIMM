class ScoreManager:
    def __init__(self):
        self.players = {}
    
    def add_player(self, name):
        if name not in self.players:
            self.players[name] = []
            return f"Added player: {name}"
        return f"Player {name} already exists"
    
    def add_score(self, name, score):
        if name in self.players:
            self.players[name].append(score)
            return f"Score {score} added for {name}"
        return f"Player {name} not found"
    
    def get_player_stats(self, name):
        if name not in self.players or not self.players[name]:
            return f"No data for {name}"
        
        scores = self.players[name]
        return {
            "total_games": len(scores),
            "average_score": round(sum(scores) / len(scores), 2),
            "best_score": max(scores),
            "worst_score": min(scores),
            "improvement": scores[-1] - scores[0] if len(scores) > 1 else 0
        }
    
    def get_leaderboard(self):
        leaderboard = []
        for name, scores in self.players.items():
            if scores:
                avg_score = sum(scores) / len(scores)
                leaderboard.append((name, round(avg_score, 2)))
        
        return sorted(leaderboard, key=lambda x: x[1], reverse=True)

# Test the system
game = ScoreManager()
print(game.add_player("Alice"))
print(game.add_player("Bob"))
print(game.add_score("Alice", 85))
print(game.add_score("Alice", 92))
print(game.add_score("Bob", 78))
print(game.add_score("Bob", 88))

print("\nPlayer Stats:")
print("Alice:", game.get_player_stats("Alice"))
print("Bob:", game.get_player_stats("Bob"))

print("\nLeaderboard:")
for rank, (name, avg) in enumerate(game.get_leaderboard(), 1):
    print(f"{rank}. {name}: {avg}")