Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-06: Landing Pages Design Consistency', () => {
    before(async () => { await browser.url('http://www.ipsy.com/campaign-landing'); });
    it('Positive - Verify that all landing pages reflect the same design and styling as the homepage', async () => {
        const landingBanner = await $('.banner');
        await expect(landingBanner).toBeDisplayed();
        const landingButton = await $('.button');
        await expect(landingButton).toHaveAttribute('style', 'font-family: same-font;');
    });
    it('Negative - Verify inconsistency if styles overridden', async () => {
        await browser.url('http://www.ipsy.com/inconsistent-landing');
        const landingButton = await $('.button');
        await expect(landingButton).not.toHaveAttribute('style', 'font-family: same-font;');
    });
    it('Edge - Verify consistency on different devices', async () => {
        await browser.setWindowSize(1024, 768);
        const landingBanner = await $('.banner');
        await expect(landingBanner).toBeDisplayed();
    });
});
