##FRIENDS ANALYSIS
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request as urllib2
import re
import urllib.request
import codecs
import time

url2 = "https://fangj.github.io/friends/season/0102.html"
url_season = "https://fangj.github.io/friends/"

#start to calculate time
start_time = time.time()

actors = ["Monica", "Joey", "Chandler", "Phoebe", "Ross", "Rachel", "All"]
regex_list = [r"\b(Monica|Joey|Chandler|Phoebe|Ross|Rachel|All):", r"\b(MONICA|JOEY|CHANDLER|PHOEBE|ROSS|RACHEL|ALL):"]

def match_actors(episode_number):
    count_dict = {}
    try:
        url = f"https://fangj.github.io/friends/season/{episode_number}.html"
        html = urllib.request.urlopen(url).read()
        html = codecs.decode(html, "unicode_escape")

        for line in html.splitlines():
            for regex in regex_list:
                actor_match = re.search(regex, line)
                if actor_match:
                    actor = actor_match.group(1).strip()
                    if actor.title() in actors:
                        count_dict[actor] = count_dict.get(actor, 0) + 1

        filtered_dict = {k.title(): v for k, v in count_dict.items()}
        return filtered_dict

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: {url} not found")
        else:
            print(f"Error: {e}")
        return

def main(episodes):
    total_dict = {}
    for episode in episodes:
        episode_data = match_actors(episode)
        value_to_add = episode_data["All"] if "All" in episode_data else 0
        for actor, lines in episode_data.items():
            if actor != "All":
                total_dict[actor] = total_dict.get(actor, 0) + lines + value_to_add
    return total_dict


episodes1 = ["0101", "0102", "0103", "0104", "0105", "0106", "0107", "0108", "0109", "0110", "0111", "0112", "0113", "0114", "0115",  "0116", "0117", "0118", "0119", "0120", "0121", "0122", "0123", "0124"]
episodes2 = ["0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209", "0210", "0211", "0212-0213", "0214", "0215", "0216", "0217", "0218", "0219", "0220", "0221", "0222", "0223", "0224"]
episodes3 = ["0301", "0302", "0303", "0304", "0305", "0306", "0307", "0308", "0309", "0310", "0311", "0312", "0313", "0314", "0315", "0316", "0317", "0318", "0319", "0320", "0321", "0322", "0323", "0324", "0325"]
episodes4 = ["0401", "0402", "0403", "0404", "0405", "0406", "0407", "0408", "0409", "0410", "0411", "0412", "0413", "0414", "0415", "0416", "0417", "0418", "0419", "0420", "0421", "0422", "0423"]
episodes5 = ["0501", "0502", "0503", "0504", "0505", "0506", "0507", "0508", "0509", "0510", "0511", "0512", "0513", "0514", "0515", "0516", "0517", "0518", "0519", "0520", "0521", "0522", "0523"]
episodes6 = ["0601", "0602", "0603", "0604", "0605", "0606", "0607", "0608", "0609", "0610", "0611", "0612", "0613", "0614", "0615-0616", "0617", "0618", "0619", "0620", "0621", "0622", "0623", "0624"]
episodes7 = ["0701", "0702", "0703", "0704", "0705", "0706", "0707", "0708", "0709", "0710", "0711", "0712", "0713", "0714", "0715", "0716", "0717", "0718", "0719", "0720", "0721", "0722", "0723"]
episodes8 = ["0801", "0802", "0803", "0804", "0805", "0806", "0807", "0808", "0809", "0810", "0811", "0812", "0813", "0814", "0815", "0816", "0817", "0818", "0819", "0820", "0821", "0822", "0823"]
episodes9 = ["0901", "0902", "0903", "0904", "0905", "0906", "0907", "0908", "0909", "0910", "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919", "0920", "0921", "0922", "0923-0924"]
episodes10 = ["1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017-1018"]
episodes_s = ["0901"]
episodes = episodes1 + episodes2 + episodes3 + episodes4 + episodes5 + episodes6 + episodes7 + episodes8 + episodes9 + episodes10
# print(type(episodes))

actors_count_dict = main(episodes)
# print(type(actors_count))
print(actors_count_dict)


def visualize_seaborn(count_dict):
    sns.set_style('whitegrid')
    sns.set_palette('deep')
    ax = sns.barplot(x=list(count_dict.keys()), y=list(count_dict.values()), alpha=0.8)
    ax.set_xlabel('Friends', fontsize=14)
    ax.set_ylabel('Number of lines', fontsize=14)
    ax.set_title('10 Seasons Actors Lines', fontsize=16)
    ax.tick_params(axis='both', labelsize=12)
    plt.show()


#end of calculating a time required to execute the code
end_time = time.time()
elapsed_time = round(end_time - start_time, 2)
print(f"Elapsed time: {elapsed_time} seconds")
print(visualize_seaborn(actors_count_dict))









