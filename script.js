// Configuration - Add your Instagram image URLs here
const ACCOUNT_A_PHOTOS = [
    'photos_heartlands.studio/downloadgram.org_568466690_18064021622594056_1240490457048692963_n.jpg',
    'photos_heartlands.studio/instagram_DHDCOUuzH2j.jpg',
    'photos_heartlands.studio/instagram_DHiCwHezOQe.jpg',
    'photos_heartlands.studio/instagram_DHmZOCMTcYN.jpg',
    'photos_heartlands.studio/instagram_DILSe-vTDEG.jpg',
    'photos_heartlands.studio/instagram_DIdRiTnT_Ro.jpg',
    'photos_heartlands.studio/instagram_DIzyhYKTWJr.jpg',
    'photos_heartlands.studio/instagram_DJ59pNWTrOX.jpg',
    'photos_heartlands.studio/instagram_DJSaIPyTvfK.jpg',
    'photos_heartlands.studio/instagram_DJWRdD6zavN.jpg',
    'photos_heartlands.studio/instagram_DJX3qNDTu1-.jpg',
    'photos_heartlands.studio/instagram_DJi2UWxzn2t.jpg',
    'photos_heartlands.studio/instagram_DJsmxkbTuCx.jpg',
    'photos_heartlands.studio/instagram_DJsrruFTSuw.jpg',
    'photos_heartlands.studio/instagram_DKDPvSWTNb1.jpg',
    'photos_heartlands.studio/instagram_DKDRInBTQLK.jpg',
    'photos_heartlands.studio/instagram_DKIxTiVT-Oc.jpg',
    'photos_heartlands.studio/instagram_DKgpPL9zw9t.jpg',
    'photos_heartlands.studio/instagram_DKocPVUTIS9.jpg',
    'photos_heartlands.studio/instagram_DLY074Cxn6C.jpg',
    'photos_heartlands.studio/instagram_DLe5cmxR7VN.jpg',
    'photos_heartlands.studio/instagram_DM9CPz8TTsg.jpg',
    'photos_heartlands.studio/instagram_DM9YDZUz3Dc.jpg',
    'photos_heartlands.studio/instagram_DMm4eV0zqbt.jpg',
    'photos_heartlands.studio/instagram_DMzYd_mTvpC.jpg',
    'photos_heartlands.studio/instagram_DN2UISWZvvm.jpg',
    'photos_heartlands.studio/instagram_DN4h-hik87B.jpg',
    'photos_heartlands.studio/instagram_DNAP6r_zZG_.jpg',
    'photos_heartlands.studio/instagram_DNFH2GVTo1i.jpg',
    'photos_heartlands.studio/instagram_DNXElEzzFa5.jpg',
    'photos_heartlands.studio/instagram_DNmvkaLTsXY.jpg',
    'photos_heartlands.studio/instagram_DNnFDebz8Zg.jpg',
    'photos_heartlands.studio/instagram_DNpqf89z0o6.jpg',
    'photos_heartlands.studio/instagram_DNsFWbl5qn4.jpg',
    'photos_heartlands.studio/instagram_DNz0aGm5kJg.jpg',
    'photos_heartlands.studio/instagram_DO5SRgLEwNE.jpg',
    'photos_heartlands.studio/instagram_DO7Za1Skz5h.jpg',
    'photos_heartlands.studio/instagram_DOGDg9ADW_v.jpg',
    'photos_heartlands.studio/instagram_DOIVJwkk24_.jpg',
    'photos_heartlands.studio/instagram_DOJ5t_-E3nk.jpg',
    'photos_heartlands.studio/instagram_DOVKVGCEokv.jpg',
    'photos_heartlands.studio/instagram_DOc89ZOE1il.jpg',
    'photos_heartlands.studio/instagram_DOxWnWyk0E6.jpg',
    'photos_heartlands.studio/instagram_DP5GMApkz36.jpg',
    'photos_heartlands.studio/instagram_DPAxwleE73j.jpg',
    'photos_heartlands.studio/instagram_DPDtA5Tk7bF.jpg',
    'photos_heartlands.studio/instagram_DPS0rJCk7sL.jpg',
    'photos_heartlands.studio/instagram_DPdMk5rkyq-.jpg',
    'photos_heartlands.studio/instagram_DPdOnmoEyRj.jpg',
    'photos_heartlands.studio/instagram_DPfymTIkzNb.jpg',
    'photos_heartlands.studio/instagram_DPhZigPE1ps.jpg',
    'photos_heartlands.studio/instagram_DPiZ0JKEzgH.jpg',
    'photos_heartlands.studio/instagram_DPxbD2sk3Ns.jpg',
];

const ACCOUNT_B_PHOTOS = [
    'photos_storytellers.studio/instagram_DH-auUWyHvf.jpg',
    'photos_storytellers.studio/instagram_DH5KMazBf8z.jpg',
    'photos_storytellers.studio/instagram_DH5UfiNBu4Z.jpg',
    'photos_storytellers.studio/instagram_DIBGbCjANoF.jpg',
    'photos_storytellers.studio/instagram_DIDkUSwu70Y.jpg',
    'photos_storytellers.studio/instagram_DILj2ebgiNW.jpg',
    'photos_storytellers.studio/instagram_DIOByHSuWSi.jpg',
    'photos_storytellers.studio/instagram_DIQqBKIA71_.jpg',
    'photos_storytellers.studio/instagram_DIdbIdcMuDv.jpg',
    'photos_storytellers.studio/instagram_DIivAzqsQt7.jpg',
    'photos_storytellers.studio/instagram_DIvjkLtNwtj.jpg',
    'photos_storytellers.studio/instagram_DJ1DS4YAK3y.jpg',
    'photos_storytellers.studio/instagram_DJ6OjQrvLR0.jpg',
    'photos_storytellers.studio/instagram_DJTmstTMV3f.jpg',
    'photos_storytellers.studio/instagram_DJWIC1zuuOZ.jpg',
    'photos_storytellers.studio/instagram_DJbVL7zsJ8O.jpg',
    'photos_storytellers.studio/instagram_DJld8DUvfHp.jpg',
    'photos_storytellers.studio/instagram_DJtWpxSt6z8.jpg',
    'photos_storytellers.studio/instagram_DJv-2ztMs27.jpg',
    'photos_storytellers.studio/instagram_DKMYWGvzRMn.jpg',
    'photos_storytellers.studio/instagram_DMKXnL7AYR8.jpg',
    'photos_storytellers.studio/instagram_DN-WQO8DcU-.jpg',
    'photos_storytellers.studio/instagram_DN0Goxr5NQB.jpg',
    'photos_storytellers.studio/instagram_DN2n3QFVDxS.jpg',
    'photos_storytellers.studio/instagram_DN5FzQujbLq.jpg',
    'photos_storytellers.studio/instagram_DN74UM7CdpV.jpg',
    'photos_storytellers.studio/instagram_DNnHxXqgZYf.jpg',
    'photos_storytellers.studio/instagram_DNpiKWsp7iy.jpg',
    'photos_storytellers.studio/instagram_DNxa7jEWHe-.jpg',
    'photos_storytellers.studio/instagram_DO-nQSujZ0Z.jpg',
    'photos_storytellers.studio/instagram_DO0a9PnAkmQ.jpg',
    'photos_storytellers.studio/instagram_DO5dqwIDQ5K.jpg',
    'photos_storytellers.studio/instagram_DO77mhMAarM.jpg',
    'photos_storytellers.studio/instagram_DODY_h3jmYv.jpg',
    'photos_storytellers.studio/instagram_DOImFjZlbLv.jpg',
    'photos_storytellers.studio/instagram_DONozzJDc4U.jpg',
    'photos_storytellers.studio/instagram_DOQQ9iQjQM6.jpg',
    'photos_storytellers.studio/instagram_DOvHL5XiB4K.jpg',
    'photos_storytellers.studio/instagram_DOxyz8cjCfC.jpg',
    'photos_storytellers.studio/instagram_DPD3u25DFx_.jpg',
    'photos_storytellers.studio/instagram_DPGcgQMDZnv.jpg',
    'photos_storytellers.studio/instagram_DPLfOrPjMWA.jpg',
    'photos_storytellers.studio/instagram_DPQliQaiiJ5.jpg',
];

// Game state
let currentRound = 1;
let scoreA = 0;
let scoreB = 0;
let usedIndicesA = [];
let usedIndicesB = [];
let currentPhotoA = null;
let currentPhotoB = null;

// DOM elements
const imgLeft = document.getElementById('img-left');
const imgRight = document.getElementById('img-right');
const photoLeft = document.getElementById('photo-left');
const photoRight = document.getElementById('photo-right');
const currentRoundEl = document.getElementById('current-round');
const gameScreen = document.getElementById('game-screen');
const resultsScreen = document.getElementById('results-screen');
const restartBtn = document.getElementById('restart-btn');

// Utility functions
function getRandomUnusedIndex(array, usedIndices) {
    const availableIndices = array
        .map((_, index) => index)
        .filter(index => !usedIndices.includes(index));

    if (availableIndices.length === 0) {
        // Reset if we've used all photos
        usedIndices.length = 0;
        return Math.floor(Math.random() * array.length);
    }

    const randomIndex = Math.floor(Math.random() * availableIndices.length);
    return availableIndices[randomIndex];
}

function loadNewRound() {
    // Get random photos from each account
    const indexA = getRandomUnusedIndex(ACCOUNT_A_PHOTOS, usedIndicesA);
    const indexB = getRandomUnusedIndex(ACCOUNT_B_PHOTOS, usedIndicesB);

    usedIndicesA.push(indexA);
    usedIndicesB.push(indexB);

    currentPhotoA = ACCOUNT_A_PHOTOS[indexA];
    currentPhotoB = ACCOUNT_B_PHOTOS[indexB];

    // Randomly decide which photo goes on which side
    const leftIsA = Math.random() < 0.5;

    if (leftIsA) {
        imgLeft.src = currentPhotoA;
        imgRight.src = currentPhotoB;
        photoLeft.dataset.account = 'A';
        photoRight.dataset.account = 'B';
    } else {
        imgLeft.src = currentPhotoB;
        imgRight.src = currentPhotoA;
        photoLeft.dataset.account = 'B';
        photoRight.dataset.account = 'A';
    }

    // Update round counter
    currentRoundEl.textContent = currentRound;
}

function handlePhotoClick(chosenAccount) {
    // Update score
    if (chosenAccount === 'A') {
        scoreA++;
    } else {
        scoreB++;
    }

    // Move to next round or show results
    if (currentRound < 20) {
        currentRound++;
        loadNewRound();
    } else {
        showResults();
    }
}

function showResults() {
    gameScreen.classList.add('hidden');
    resultsScreen.classList.remove('hidden');

    const totalRounds = 20;
    const percentageA = Math.round((scoreA / totalRounds) * 100);
    const percentageB = Math.round((scoreB / totalRounds) * 100);

    document.getElementById('score-a').textContent = scoreA;
    document.getElementById('score-b').textContent = scoreB;
    document.getElementById('percentage-a').textContent = `${percentageA}%`;
    document.getElementById('percentage-b').textContent = `${percentageB}%`;
}

function resetGame() {
    currentRound = 1;
    scoreA = 0;
    scoreB = 0;
    usedIndicesA = [];
    usedIndicesB = [];

    resultsScreen.classList.add('hidden');
    gameScreen.classList.remove('hidden');

    loadNewRound();
}

// Event listeners
photoLeft.addEventListener('click', () => {
    handlePhotoClick(photoLeft.dataset.account);
});

photoRight.addEventListener('click', () => {
    handlePhotoClick(photoRight.dataset.account);
});

restartBtn.addEventListener('click', resetGame);

// Initialize game
loadNewRound();
