from bs4 import BeautifulSoup
import requests

banks = [
    {
    "name": "absa" ,
    "urls": {
        "home": "https://www.absa.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "capitec" ,
    "urls": {
        "home_url": "https://www.capitecbank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "standardbank" ,
    "urls": {
        "home_url": "https://www.standardbank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "fnb" ,
    "urls": {
        "home_url": "https://www.fnb.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "nedbank" ,
    "urls": {
        "home_url": "https://www.nedbank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "investec" ,
    "urls": {
        "home_url": "https://www.investec.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "tymebank" ,
    "urls": {
        "home_url": "https://www.tymebank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    }, 
    {
    "name": "bidvestbank" ,
    "urls": {
        "home_url": "https://www.bidvestbank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    },
    {
    "name": "sasfin" ,
    "urls": {
        "home_url": "https://www.sasfin.com/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "major"
    },
    {
    "name": "mercantile" ,
    "urls": {
        "home_url": "https://www.mercantile.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "minor"
    },
    {
    "name": "grindrodbank" ,
    "urls": {
        "home_url": "https://www.grindrodbank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "minor"
    },
    {
    "name": "grobank" ,
    "urls": {
        "home_url": "https://www.grobank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "minor"
    },
    {
    "name": "hbzbank" ,
    "urls": {
        "home_url": "https://www.hbzbank.co.za/",
        "personal_accounts": "",
        "business_accounts": "",
        "investments": "",
    },
    "ranking": "minor"
    }
]

retailers = {
    "food": [
        {
        "name": "Shoprite" ,
        "urls": {
            "home_url": "https://www.shoprite.co.za/"
        }
        },
        {
        "name": "Pick n Pay" ,
        "urls": {
            "home_url": "https://www.picknpay.co.za/"
        }
        },
        {
        "name": "Spar" ,
        "urls": {
            "home_url": "https://www.spar.co.za/"
        }
        },
        {
        "name": "Woolworths" ,
        "urls": {
            "home_url": "https://www.woolworths.co.za/"
        }
        },
        {
        "name": "Checkers" ,
        "urls": {
            "home_url": "https://www.checkers.co.za/"
        }
        },
        {
        "name": "Makro" ,
        "urls": {
            "home_url": "https://www.makro.co.za/"
        }
        },
        {
        "name": "Food Lover's Market" ,
        "urls": {
            "home_url": "https://www.foodloversmarket.co.za/"
        }
        },
        {
        "name": "Game" ,
        "urls": {
            "home_url": "https://www.game.co.za/"
        }
        }
    ],
    "pharmacutical": [
        {
        "name": "Clicks" ,
        "urls": {
            "home_url": "https://clicks.co.za/"
        },
        }
        {
        "name": "Dis-Chem" ,
        "urls": {
            "home_url": "https://www.dischem.co.za/"
        }
        },
        {
        "name": "Pick n Pay Pharmacy" ,
        "urls": {
            "home_url": "https://www.picknpay.co.za/pharmacy
        }"
        },
        {
        "name": "Checkers Pharmacy" ,
        "urls": {
            "home_url": "https://www.checkers.co.za/pharmacy
        }"
        },
        {
        "name": "Medicare Pharmacy" ,
        "urls": {
            "home_url": "https://www.medirite.co.za/"
        }
        },
        {
        "name": "" ,
        "urls": {
            "home_url": ""
        },
        {
        "name": "" ,
        }
        "urls": {
            "home_url": ""
        }
    ],
    "clothing":[
        {
        "name
        }": "Woolworths" ,
        "urls": {
            "home_url": "https://www.woolworths.co.za/"
        }
        },
        {
        "name": "Edgars" ,
        "urls": {
            "home_url": "https://www.edgars.co.za/"
        }
        },
        {
        "name": "Truworths" ,
        "urls": {
            "home_url": "https://www.truworths.co.za/"
        }
        },
        {
        "name": "Foschini" ,
        "urls": {
            "home_url": "https://www.foschini.co.za/"
        }
        },
        {
        "name": "Mr Price" ,
        "urls": {
            "home_url": "https://www.mrp.com/"
        },
        }
        {
        "name": "Cotton On" ,
        "urls": {
            "home_url": "https://cottonon.com/ZA/"
        },
        }
        {
        "name": "H&M" ,
        "urls": {
            "home_url": "https://www.hm.com/za"
        }
        },
        {
        "name": "Zara" ,
        "urls": {
            "home_url": "https://www.zara.com/za/"
        }
        },
        {
        "name": "Ackermans" ,
        "urls": {
            "home_url": "https://www.ackermans.co.za/"
        }
        },
        {
        "name": "Pick n Pay Clothing" ,
        "urls": {
            "home_url": "https://www.picknpay.co.za/clothing
        }"
        },
        {
        "name": "Jet" ,
        "urls": {
            "home_url": "https://www.jetonline.co.za/"
        }
        },
        {
        "name":"Pep" ,
        "urls": {
            "home_url": "https://www.pepstores.com/"
        },
        }
    ]
}

